// 这个示例程序展示如何序列化JSON字符串
package main

import (
	"encoding/json"
	"fmt"
	"log"
)

func main() {
	// 创建一个保存键值对的映射
	c := make(map[string]interface{})
	c["name"] = "Gopher"
	c["title"] = "programmer"
	c["contact"] = map[string]interface{}{
		"home": "415.333.3333",
		"cell": "415.555.5555",
	}

	// 将这个映射序列化到JSON字符串
	// MarshalIndent函数将一个map值转换为一个JSON字符串
	data, err := json.MarshalIndent(c, "", " ")
	// data, err := json.Marshal(c)
	if err != nil {
		log.Println("ERROR:", err)
		return
	}
	fmt.Println(string(data))
	fmt.Printf("%T\n", data)
	fmt.Printf("%T\n", string(data))
}
