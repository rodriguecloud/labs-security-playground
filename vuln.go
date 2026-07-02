package main

import (
	"fmt"
	"os/exec"
)

func pingHost() {
	var host string
	fmt.Print("Enter the host address to ping: ")
	fmt.Scanln(&host)

	// VULNERABILITY: Using "sh -c" with concatenated input.
	// This forces Go to invoke the system shell, which interprets special characters.
	// Malicious input example: "8.8.8.8; cat /etc/passwd"
	command := "ping -c 1 " + host
	cmd := exec.Command("sh", "-c", command)

	output, err := cmd.CombinedOutput()
	if err != nil {
		fmt.Printf("Error: %s\n", err)
	}
	fmt.Printf("Output: %s\n", string(output))
}

func main() {
	pingHost()
}
