### Go 语言学习



>  **defer**

defer语句调用一个函数，这个函数会推迟执行，直到外围函数返回，或者外围函数运行到最后，或者相应的goroutine panic

**函数值和函数参数被求值，但函数不会立即调用**

```
func trace(funcName string) func(){
    start := time.Now()
    fmt.Printf("function %s enter\n",funcName)
    return func(){
        log.Printf("function %s exit (elapsed %s)",funcName,time.Since(start))
    }
}
 
func foo(){
    defer trace("foo()")()
    time.Sleep(5*time.Second)
}
func main(){
    foo()
    foo()
}
/*
OUTPUT:
function foo() enter
function foo() exit (elapsed 5.0095471s)
function foo() enter
function foo() exit (elapsed 5.0005382s)
*/

defer后面的函数值和参数会被求值但是实际函数调用却要等到最后
```



**存在多个defer语句，最后的defer的函数的执行顺序与defer出现的顺序相反**

```
func main() {
    func1 := func(){
        fmt.Println("func1() execution deferred")
    }
    func2 := func(){
        fmt.Println("func2() execution deferred")
    }
    defer func1()
    defer func2()
    fmt.Println("strat\nworking...")
}
/*
OUTPUT:
strat
working...
func2() execution deferred
func1() execution deferred
*/

```





> Goroutine

并发机制，在函数调用语句前添加 go关键字，可创建并发执行单元。







> 交叉编译

编译 linux 上的程序

 ```
GOOS=linux GOARCH=amd64 go build 
 ```



```
GOOS=linux GOARCH=amd64 go build -o /Users/weicheng/goProject/bin/log2dfskind /Users/weicheng/goProject/src/aiur/app/log2dfskind/main.go


GOOS=linux GOARCH=amd64 go build -o /Users/weicheng/goProject/bin/log2dfs /Users/weicheng/goProject/src/aiur/app/log2dfs/main.go


GOOS=linux GOARCH=amd64 go build -o /Users/weicheng/goProject/bin/dataClean /Users/weicheng/goProject/src/aiur/app/logcleanes/dataClean.go
```





> 类型转换

不⽀支持隐式类型转换，即便是从窄向宽转换

不能将其他类型当 bool