package main
import "fmt"

func main() {
	// 创建一个映射，键的类型是string，值的类型是int。
	dict := make(map[string]int)
	fmt.Println("case1: ", dict)
	// 创建一个映射，键值的类型都是string并初始化两个值
	dict1 := map[string]string{"Red": "#da1337", "Orange": "#e95a22"}
	fmt.Println("case2: ", dict1)

	// 创建一个空映射，存储颜色及其对应的十六进制代码
	colors := map[string]string{}
	// 加red的代码进入映射
	colors["Red"] = "#da1337"
	fmt.Println("case3: ", colors)


	// 创建一个nil映射
	var colors3 map[string]string
	fmt.Println("case4: ", colors3)
	// colors2["Red"] = "#da1337" // 这个会报错

	// 判断键是否存在：
	value, exists := colors["Blue"]
	fmt.Println("case5: ", value, exists)
	if exists {
		fmt.Println("case5: ", value)
	}

	// 显示映射中的所有颜色
	fmt.Println("case6")
	colors["AliceBlue"] = "#f0f8ff"
	colors["Coral"] = "#ff7F50"
	colors["DarkGrey"] = "#a9a9a9"
	colors["ForestGreen"] = "#228b22"
	for key, value := range colors {
		fmt.Printf("Key: %s, Value: %s\n", key, value)
	}
	
	// 删除一个键值对
	delete(colors, "Coral")
	fmt.Println(colors)
}