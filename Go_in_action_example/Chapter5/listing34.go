// 这个示例程序展示如何使用io.Reader和io.Writer接口
// 写一个简单版本的curl程序
package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
)

// init在main函数之前嗲用
func init() {
	if len(os.Args) != 2 {
		fmt.Println("Usage: ./example2 <url>")
		os.Exit(-1)
	}
}

// main是应用程序的入口
func main() {
	// 从web服务器得到响应
	r, err := http.Get(os.Args[1])
	if err != nil {
		fmt.Println(err)
		return
	}

	// 从body复制到stdout
	io.Copy(os.Stdout, r.Body)
	if err := r.Body.Close(); err != nil {
		fmt.Println(err)
	}
}

// run
// go run .\listing34.go https://www.baidu.com

// run with error
// go run .\listing34.go
