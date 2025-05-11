package greetings

import (
	"errors"
	"fmt"
	"math/rand"
)

func Hello(name string) (string, error) {
	if name == "" {
		return "", errors.New("empty name")
	}
	messege := fmt.Sprintf(randomStrings(), name)
	return messege, nil
}

func randomStrings() string {
	format := []string{
		"Hi, %v",
		"Hello, %v",
	}
	return format[rand.Intn(len(format))]
}

func Hellos(names []string) (map[string]string, error) {
	messages := map[string]string{}
	for index, name := range names {
		fmt.Println(index)
		message, err := Hello(name)
		if err != nil {
			return nil, err
		}

		messages[name] = message

	}

	return messages, nil
}
