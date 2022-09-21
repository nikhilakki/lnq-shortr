import { useMsal } from "@azure/msal-react"

export function WelcomeUser() {
  const { accounts } = useMsal()
  const username = accounts[0].username

  return <p>Welcome, {username}</p>
}
export default function SignInBtn() {
  // useMsal hook will return the PublicClientApplication instance you provided to MsalProvider
  const { instance } = useMsal()

  return <button onClick={() => instance.loginRedirect()}>Sign In</button>
}
