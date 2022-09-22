// Copyright (c) 2022 Nikhil Akki
//
// This software is released under the MIT License.
// https://opensource.org/licenses/MIT

export async function callApi(accessToken: string, url: string) {
  const reqOptions = {
    method: "GET",
    headers: new Headers({
      Authorization: "Bearer " + accessToken,
      // "Content-Type": "application/x-www-form-urlencoded",
    }),
  }
  const response = await fetch(url, reqOptions)
    .then((res) => res.json())
    .catch((err) => console.error(err))
  return response
}

const CONFIG = {
  BACKEND_URL: process.env.BACKEND_URL || "http://localhost:8000",
  FRONTEND_URL: process.env.FRONTEND_URL || "http://localhost:3000",
}

// console.log({ CONFIG })
export default CONFIG
