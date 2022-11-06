// Copyright (c) 2022 Nikhil Akki
// 
// This software is released under the MIT License.
// https://opensource.org/licenses/MIT


package main

import (
    "log"

    "github.com/gofiber/fiber/v2"

	"database/sql"

	_ "github.com/lib/pq"
)

func main() {
    app := fiber.New()
	connStr := "user=pqgotest dbname=pqgotest sslmode=verify-full"
	db, err := sql.Open("postgres", connStr)
	if err != nil {
		log.Fatal(err)
	}

	app.Get("/ping", func (c *fiber.Ctx) error {
        return c.SendString("Ping ping!")
    })
    app.Get("/:url", func (c *fiber.Ctx) error {
		url := c.Params("url")
		rows, err := db.Query("SELECT long_url FROM urls WHERE short_url = $1", url)
		fmt.Println(rows)
        return c.Redirect(rows)
    })

    log.Fatal(app.Listen(":5000"))
}