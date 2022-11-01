// Copyright (c) 2022 Nikhil Akki
//
// This software is released under the MIT License.
// https://opensource.org/licenses/MIT
import { useSession, signIn, signOut } from "next-auth/react"

export default function LoginComponent() {
  const { data: session } = useSession()
  if (session) {
    return (
      <>
        Signed in as {session.user.email} <br />
        <button onClick={() => signOut()}>Sign out</button>
      </>
    )
  }
  return (
    <>
      Not signed in <br />
      <button onClick={() => signIn()}>Sign in</button>
    </>
  )
}
