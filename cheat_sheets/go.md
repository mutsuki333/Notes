# Go Cheat Sheet

### Default values

**Option 1:** The caller chooses to use default values

```go
// Both parameters are optional, use empty string for default value
func Concat1(a string, b int) string {
  if a == "" {
    a = "default-a"
  }
  if b == 0 {
    b = 5
  }

  return fmt.Sprintf("%s%d", a, b)
}
```

**Option 2:** A single optional parameter at the end

```go
// a is required, b is optional.
// Only the first value in b_optional will be used.
func Concat2(a string, b_optional ...int) string {
  b := 5
  if len(b_optional) > 0 {
    b = b_optional[0]
  }

  return fmt.Sprintf("%s%d", a, b)
}
```

**Option 3:** A config struct

```go
// A declarative default value syntax
// Empty values will be replaced with defaults
type Parameters struct {
  A string `default:"default-a"` // this only works with strings
  B string // default is 5
}

func Concat3(prm Parameters) string {
  typ := reflect.TypeOf(prm)

  if prm.A == "" {
    f, _ := typ.FieldByName("A")
    prm.A = f.Tag.Get("default")
  }

  if prm.B == 0 {
    prm.B = 5
  }

  return fmt.Sprintf("%s%d", prm.A, prm.B)
}
```

**Option 4:** Full variadic argument parsing (javascript style)

```go
func Concat4(args ...interface{}) string {
  a := "default-a"
  b := 5

  for _, arg := range args {
    switch t := arg.(type) {
      case string:
        a = t
      case int:
        b = t
      default:
        panic("Unknown argument")
    }
  }

  return fmt.Sprintf("%s%d", a, b)
}
```

### inspect build app 

`go tool nm ./main | grep XXX`
