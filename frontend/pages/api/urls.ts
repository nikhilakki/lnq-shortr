// Copyright (c) 2022 Nikhil Akki
//
// This software is released under the MIT License.
// https://opensource.org/licenses/MIT

import { unstable_getServerSession } from "next-auth/next"
import { authOptions } from "./auth/[...nextauth]"
import CONFIG from "../../utils"

export default async (req, res) => {
  console.log({ req })
  const session = await unstable_getServerSession(req, res, authOptions)
  const { name, url, user_id } = req.body
  console.log({ name, url, user_id })
  if (session) {
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, url, user_id: user_id }),
    }
    const response = await fetch(
      `${CONFIG.BACKEND_URL}/short-url`,
      requestOptions
    )
      .then((data) => data.json())
      .catch((err) => console.error(err))
    console.log({ response })
    res.send({
      content: response,
    })
  } else {
    res.send({
      error:
        "You must be signed in to view the protected content on this page.",
    })
  }
}
