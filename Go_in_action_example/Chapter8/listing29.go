// 这个示例程序展示如何解码JSON字符串
package main

import (
	"encoding/json"
	"fmt"
	"log"
)

// JSON 包含用于反序列化的演示字符串
// 先把JSON文档保存在一个字符串变量里
var JSON = `{
	"name": "Gopher",
	"title": "programmer",
	"contact": {
		"home": "415.333.3333",
		"cell": "415.555.5555"	
	}
}`

func main() {
	// 将JSON字符串反序列化到map变量
	// 变量c声明为为一个map类型，key是string类型，value是interface{}类型
	var c map[string]interface{}
	err := json.Unmarshal([]byte(JSON), &c)
	if err != nil {
		log.Println("ERROR:", err)
		return
	}
	// fmt.Println(c)
	// 这个冒号后面不需要用空格，会自动有个空格输出在Name:和c["name"]中间
	fmt.Println("Name:", c["name"])
	fmt.Println("Title:", c["title"])
	fmt.Println("Contact")
	fmt.Println("H:", c["contact"].(map[string]interface{})["home"])
	fmt.Println("C:", c["contact"].(map[string]interface{})["cell"])
}
