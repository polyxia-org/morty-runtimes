package main

import (
	"handler/function"
	"log"
	"net/http"
)

func main() {
	s := &http.Server{
		Addr:           ":3000",
	}
	http.HandleFunc("/", function.Handler)

	if err := s.ListenAndServe(); err != nil {
		log.Fatal(err)
	}
}