// Copyright (c) 2022 Nikhil Akki
//
// This software is released under the MIT License.
// https://opensource.org/licenses/MIT
import { getCsrfToken } from "next-auth/react"

export default function AccessTokenComponent() {
  const token = getCsrfToken()
  console.log({ token })
  // const { accessToken } = token

  // return <div>Access Token: {accessToken}</div>
}
