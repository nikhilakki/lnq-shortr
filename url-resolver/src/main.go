package main

import (
	"log"
	"os"

	"github.com/gofiber/fiber/v2"

	"database/sql"

	_ "github.com/lib/pq"
)

func main() {
	app := fiber.New()
	connStr := os.Getenv("PGSQL")
	db, err := sql.Open("postgres", connStr)
	if err != nil {
		log.Fatal(err)
	}
	app.Get("/ping", func(c *fiber.Ctx) error {
		if err != nil {
			log.Fatal(err)
		}
		return c.SendString("Hello world")
	})

	app.Get("/:url", func(c *fiber.Ctx) error {
		url := c.Params("url")
		var long_url string
		rows, err := db.Query("select lu.long_url  from landing_url lu where lu.short_url = $1", url)
		if err != nil {
			log.Fatal(err)
		}
		defer rows.Close()
		for rows.Next() {
			err := rows.Scan(&long_url)
			if err != nil {
				panic(err)
			}
			log.Println("\n", long_url)
			
		}
		err = rows.Err()
		if err != nil {
			panic(err)
		}
		return c.Redirect(long_url)
		})

	log.Fatal(app.Listen("0.0.0.0:5000"))
}
