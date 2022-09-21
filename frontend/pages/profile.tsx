// Copyright (c) 2022 Nikhil Akki
//
// This software is released under the MIT License.
// https://opensource.org/licenses/MIT

import {
  InteractionRequiredAuthError,
  InteractionStatus,
} from "@azure/msal-browser"
import { AuthenticatedTemplate, useMsal } from "@azure/msal-react"
import { useEffect, useState } from "react"

async function callApi(accessToken: string) {
  console.log({ accessToken })
  return { response: accessToken }
}
function ProtectedComponent() {
  const { instance, inProgress, accounts } = useMsal()
  const [apiData, setApiData] = useState([])

  console.log({ inProgress, accounts })
  useEffect(() => {
    if (!apiData && inProgress === InteractionStatus.None) {
      const accessTokenRequest = {
        scopes: ["user.read"],
        account: accounts[0],
      }
      instance
        .acquireTokenSilent(accessTokenRequest)
        .then((accessTokenResponse) => {
          // Acquire token silent success
          let accessToken = accessTokenResponse.accessToken
          // Call your API with token
          callApi(accessToken).then((response) => {
            setApiData(response)
          })
        })
        .catch((error) => {
          if (error instanceof InteractionRequiredAuthError) {
            instance
              .acquireTokenPopup(accessTokenRequest)
              .then(function (accessTokenResponse) {
                // Acquire token interactive success
                let accessToken = accessTokenResponse.accessToken
                // Call your API with token
                callApi(accessToken).then((response) => {
                  setApiData(response)
                })
              })
              .catch(function (error) {
                // Acquire token interactive failure
                console.log(error)
              })
          }
          console.log(error)
        })
    }
  }, [instance, accounts, inProgress, apiData])

  return <p>Return your protected content here: {apiData}</p>
}

export default function Profile() {
  return (
    <AuthenticatedTemplate>
      <ProtectedComponent />
    </AuthenticatedTemplate>
  )
}
