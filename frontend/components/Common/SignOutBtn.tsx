// Copyright (c) 2022 Nikhil Akki
//
// This software is released under the MIT License.
// https://opensource.org/licenses/MIT

import { useMsal } from "@azure/msal-react"

// SignOutButton Component returns a button that invokes a redirect logout when clicked
export default function SignOutButton() {
  // useMsal hook will return the PublicClientApplication instance you provided to MsalProvider
  const { instance } = useMsal()
  console.log({ instance })
  return (
    <button
      onClick={() => instance.logoutRedirect({ postLogoutRedirectUri: "/" })}
    >
      Sign Out
    </button>
  )
}
