To resolve the following error (only exists on nixos I think)

`unknown type name 'uint_farptr_t'; did you mean 'uint_fast8_t'?`

add this to `.clangd`

```
CompileFlags:
  Add:
    - -isystem/home/raphael/.platformio/packages/toolchain-atmelavr/avr/include
```
