package main

import (
	"fmt"
	"io/ioutil"
	"os"

	// "./words"
	"github.com/goinaction/code/chapter3/words"
)

// main是程序的入口
func main() {
	filename := os.Args[1]

	contents, err := ioutil.ReadFile(filename)
	if err != nil {
		fmt.Println(err)
		return
	}

	text := string(contents)

	count := words.CountWords(text)
	fmt.Printf("There are %d words in your text. \n", count)
}
