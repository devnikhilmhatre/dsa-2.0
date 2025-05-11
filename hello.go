package main

import (
	"fmt"
	"time"
)

// SafeCounter is safe to use concurrently.
type SafeCounter struct {
	// mu sync.Mutex
	v map[string]int
}

// Inc increments the counter for the given key.
func (c *SafeCounter) Inc(key string, i int) {
	fmt.Println(i, key)
	// c.mu.Lock()
	// Lock so only one goroutine at a time can access the map c.v.
	c.v[key]++
	// c.mu.Unlock()
}

// Value returns the current value of the counter for the given key.
func (c *SafeCounter) Value(key string) int {
	fmt.Println(key, "value")
	// c.mu.Lock()
	// Lock so only one goroutine at a time can access the map c.v.
	// defer c.mu.Unlock()
	return c.v[key]
}

func main() {
	c := SafeCounter{v: make(map[string]int)}
	for i := 0; i < 100; i++ {
		go c.Inc("somekey", i)
	}

	fmt.Println("For Done .......................................................")

	time.Sleep(time.Second)
	fmt.Println("Sleep Done .....................................................")
	fmt.Println(c.Value("somekey"))
}
