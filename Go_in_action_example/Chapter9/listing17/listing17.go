// 这个示例程序实现了简单的网络服务
package main

import (
	"log"
	"net/http"

	"./handlers"
)

// main is the entry point for the application.
// 在http://localhost:4000/sendjson可以看到handlers包中的json文档
func main() {
	handlers.Routes()

	log.Println("listener : Started : Listening on :4000")
	http.ListenAndServe(":4000", nil)
}
