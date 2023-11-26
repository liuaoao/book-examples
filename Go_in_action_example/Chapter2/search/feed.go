package search

import (
	"encoding/json"
	"os"
)

const dataFile = "data/data.json"

// Feed contains information we need to process a feed.
// Feed包含了我们需要处理的数据源的信息
type Feed struct {
	Name string `json:"site"`
	URI  string `json:"link"`
	Type string `json:"type"`
}

// RetrieveFeeds reads and unmarshals the feed data file.
// RetrieveFeeds读取并反序列化 源数据文件
func RetrieveFeeds() ([]*Feed, error) {
	// Open the file.
	file, err := os.Open(dataFile)
	if err != nil {
		return nil, err
	}

	// Schedule the file to be closed once
	// the function returns.
	// 当函数返回时关闭文件
	defer file.Close()

	// Decode the file into a slice of pointers
	// to Feed values.
	// 将文件解码到一个切片里
	// 这个切片的每一项都是一个只想一个Feed类型值的指针
	var feeds []*Feed
	err = json.NewDecoder(file).Decode(&feeds)

	// We don't need to check for errors, the caller can do this.
	return feeds, err
}