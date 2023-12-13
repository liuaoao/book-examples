// 这个示例程序展示如何使用json包和NewDecoder函数
// 来解码JSON响应
package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
)

type (
	// gResult 映射到从搜索拿到的结果文档
	gResult struct {
		GsearchResultClass string `json:"GsearchResultClass"`
		UnescapedURL       string `json:"unescapedUrl"`
		URL                string `json:"url"`
		VisiableURL        string `json:"visibleUrl"`
		CacheURL           string `json:"cacheUrl"`
		Title              string `json:"title"`
		TitleNoFormatting  string `json:"titleNoFormatting"`
		Content            string `json:"content"`
	}

	// gResponse包含顶级文档
	gResponse struct {
		ResponseDara struct {
			Results []gResult `json:"results"`
		} `json:"responseData"`
	}
)

func main() {
	uri := "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&rsz=8&q=golang"

	// 向google发起搜索
	resp, err := http.Get(uri)
	if err != nil {
		log.Println("ERROR1:", err)
		return
	}
	fmt.Println(resp.Body)
	defer resp.Body.Close()

	// 将JSON响应解码到结构类型
	var gr gResponse
	err = json.NewDecoder(resp.Body).Decode(&gr)
	if err != nil {
		log.Println("ERROR2:", err)
		return
	}

	fmt.Println(gr)
}
