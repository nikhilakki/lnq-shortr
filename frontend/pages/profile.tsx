// Copyright (c) 2022 Nikhil Akki
//
// This software is released under the MIT License.
// https://opensource.org/licenses/MIT

import { useMsal } from "@azure/msal-react"
import { useState } from "react"

export default function ProfileContent() {
  const { instance, accounts, inProgress } = useMsal()
  const [accessToken, setAccessToken] = useState(null)

  const name = accounts[0] && accounts[0].name

  function RequestAccessToken() {
    const request = {
      ...loginRequest,
      account: accounts[0],
    }

    // Silently acquires an access token which is then attached to a request for Microsoft Graph data
    instance
      .acquireTokenSilent(request)
      .then((response) => {
        setAccessToken(response.accessToken)
      })
      .catch((e) => {
        instance.acquireTokenPopup(request).then((response) => {
          setAccessToken(response.accessToken)
        })
      })
  }

  return (
    <>
      <h5 className="card-title">Welcome {name}</h5>
      {accessToken ? (
        <p>Access Token Acquired!</p>
      ) : (
        <button onClick={RequestAccessToken}>Request Access Token</button>
      )}
    </>
  )
}
