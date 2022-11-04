// Copyright (c) 2022 Nikhil Akki
//
// This software is released under the MIT License.
// https://opensource.org/licenses/MIT
import { useSession, signIn, signOut } from "next-auth/react"
import { useState } from "react"
import axios from "axios"

export default function LoginComponent() {
  const [userID, setUserID] = useState("")
  const { data: session } = useSession()

  const fetchUserId = async (email: string) => {
    const userID = await axios.post("http://localhost:8000/user/find-user-id", {
      email: email,
    })
    return userID?.data
  }
  if (session) {
    if (userID === "") {
      const user_id = async () => {
        const res = await fetchUserId(session.user?.email)
        console.log({ res })
        setUserID(userID)
        localStorage.setItem("user_id", userID)
      }
    }
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
