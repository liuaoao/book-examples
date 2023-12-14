// 这个示例程序展示如何使用最基本的log包
package main

import (
	"log"
)

func init() {
	log.SetPrefix("TRACE: ")
	log.SetFlags(log.Ldate | log.Lmicroseconds | log.Llongfile)
}

func main() {
	// Println写到标准日志记录器
	log.Println("message")

	// Fatalln在调用Println()之后会接着调用osExit(1)
	// log.Fatalln("fatal message")

	// Panicln在调用Println之后会接着调用panic()
	log.Panicln("panic message")
}
