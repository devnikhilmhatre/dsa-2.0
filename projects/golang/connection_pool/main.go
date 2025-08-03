package main

import (
	"errors"
	"fmt"
)

var ErrNotFound = errors.New("not found")

func findUser() error {
	return fmt.Errorf("user lookup failed: %w", ErrNotFound)
}

func main() {
	err := findUser()
	if errors.Is(err, ErrNotFound) {
		fmt.Println("User was not found")
	}
}
