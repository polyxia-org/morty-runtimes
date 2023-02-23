package function

import (
	"fmt"
	"net/http"
	"encoding/json"
)

func Handler (w http.ResponseWriter, r *http.Request) {
	fmt.Println("Hello, World!")
	
	w.Header().Set("Content-Type", "application/json; charset=utf-8")
	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(map[string]string{"message": "Hello, World!"})
}
