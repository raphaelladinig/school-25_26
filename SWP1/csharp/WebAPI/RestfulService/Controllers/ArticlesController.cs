using Microsoft.AspNetCore.Mvc;
using Models;
using ORM.Services;

namespace RestfulService.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ArticlesController : ControllerBase
    {
        private readonly DbManager _dbManager;
    
        public ArticlesController(DbManager dbManager)
        { 
            _dbManager = dbManager;
        }

        [HttpGet]
        public async Task<IActionResult> GetArticles()
        {
            var articles = await _dbManager.GetArticlesAsync();
            if (articles.Count is 0) 
                return NoContent();
            return Ok(articles);
        }

        [HttpGet("{id}")]
        public async Task<IActionResult> GetArticle(int id)
        {
            var article = await _dbManager.GetArticleAsync(id);
            if (article is null) 
                return NotFound();
            return Ok(article);
        }

        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteArticle(int id)
        {
            var result = await _dbManager.DeleteArticleAsync(id);
            if (!result) 
                return NotFound();
            return NoContent();
        }

        [HttpPost]
        public async Task<IActionResult> PostArticle(Article article)
        {
            if (!ModelState.IsValid)
                return BadRequest(ModelState);
            var result = await _dbManager.AddArticleAsync(article);
            if (article is null)
                return NoContent();
            return Created(new Uri($"{Request.Scheme}://{Request.Host}{Request.Path}/{result.Id}"), article);
        }

        [HttpPut]
        public async Task<IActionResult> PutArticle(Article article)
        {
            if (!ModelState.IsValid)
                return BadRequest(ModelState);
            var result = await _dbManager.UpdateArticleAsync(article);
            if (article.Id == result.Id)
                return Created(new Uri($"{Request.Scheme}://{Request.Host}{Request.Path}/{result.Id}"), article);
            if (article is null)
                return NoContent();
            return Ok();
        }
    }
}
