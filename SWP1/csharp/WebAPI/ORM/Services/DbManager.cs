using Microsoft.EntityFrameworkCore;
using Models;

namespace ORM.Services;

public class DbManager : DbContext
{
    public DbSet<Article> Articles { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        string connectionString = "Server=localhost;Database=swp;User=root;Password=root;";
        optionsBuilder.UseMySql(connectionString, ServerVersion.AutoDetect(connectionString));
    }

    public async Task<List<Article>> GetArticlesAsync()
    {
        return await Articles.ToListAsync();
    }
    
    public async Task<Article> GetArticleAsync(int id)
    {
        var article = await Articles.FindAsync(id);
        if (article is null)
            return null;
        return article;
    }
    
    public async Task<Boolean> DeleteArticleAsync(int id)
    {
        var article = await GetArticleAsync(id);
        if (article is null)
            return false;
        Articles.Remove(article);
        return await SaveChangesAsync() > 0;
    }
    
    public async Task<Article?> AddArticleAsync(Article article)
    {
        var result = (await Articles.AddAsync(article)).Entity;;
        if (await SaveChangesAsync() > 0)
        {
            return result;
        }
        return null;
    }
    
    public async Task<Article?> UpdateArticleAsync(Article article)
    {
        if (!Articles.Contains(article))
        {
            var createdResult = await AddArticleAsync(article);
            return createdResult;
        }
        var result = Articles.Update(article).Entity;
        if (await SaveChangesAsync() > 0)
        {
            return result;
        }
        return null;
    }
}
