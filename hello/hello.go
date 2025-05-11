package main

import (
	"devnikhilmhatre/dsa/greetings"
	"fmt"
	"log"
)

func main() {

	messages, err := greetings.Hellos([]string{"Nikhil", "Mhatre"})
	if err != nil {
		log.Fatal(err)
	}

	for key, message := range messages {
		fmt.Println(key, "|", message)
	}
}
