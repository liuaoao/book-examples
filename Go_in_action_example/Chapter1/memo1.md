# 第一章：关于Go语言的介绍
1. 源代码在：https://github/com/goinaction/code下载
2. Go语言的特点：
* 高性能的语言，同事也让开发更快速
* 语法简洁到只有几个关键字，便于记忆
* 编译器速度非常快
* 类型系统简单且高效：灵活、无继承的类型系统，但依然支持面向对象开发
* 自带垃圾回收期，不需要用户自己管理内存
* 对并发的支持：goroutine、通道（channel）
3. Go Playground：http://play.golang.org 可以在浏览器中编辑并运行Go语言代码
```Go
# Go程序都组织成包
package main
# import语句用于导入外部代码，标准库中的fmt包用于格式化并输出数据
import "fmt"
# 像C语言一样，main函数是程序执行的入口
func main() {
	fmt.Println("Hello, World!")
}

```