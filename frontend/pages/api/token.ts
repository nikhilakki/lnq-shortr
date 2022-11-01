// Copyright (c) 2022 Nikhil Akki
//
// This software is released under the MIT License.
// https://opensource.org/licenses/MIT

import { getCsrfToken } from "next-auth/react"
import { NextRequest, NextResponse } from "next/server"

export default async (res: NextRequest, req: NextResponse) => {
  const token = await getCsrfToken()
  console.log({ token })
  return token
}
