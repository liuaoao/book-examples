// Package handlers 提供了用于网络服务的复古舞断电
package handlers

import (
	"encoding/json"
	"net/http"
)

// Routes 为网络服务设置路由
func Routes() {
	http.HandleFunc("/sendjson", SendJSON)
}

// SendJSON 返回了一个简单的JSON文档
func SendJSON(rw http.ResponseWriter, r *http.Request) {
	u := struct {
		Name  string
		Email string
	}{
		Name:  "Bill",
		Email: "bill@ardanstudios.com",
	}

	rw.Header().Set("Content-Type", "application/json")
	rw.WriteHeader(200)
	json.NewEncoder(rw).Encode(&u)
}