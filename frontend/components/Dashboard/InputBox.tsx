// Copyright (c) 2022 Nikhil Akki
//
// This software is released under the MIT License.
// https://opensource.org/licenses/MIT

import { useEffect, useState } from "react"
import CONFIG from "../../utils"

const InputBox = (props) => {
  const [generateClick, setGenerateClick] = useState(true)
  const [name, setName] = useState("")
  const [url, setUrl] = useState("")

  const handleClick = async () => {
    setGenerateClick(true)
    props.setLoading(true)
  }

  useEffect(() => {
    const callApi = async () => {
      // console.log({ name, url })
      if (url?.length > 0) {
        const requestOptions = {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ name, url }),
        }
        const response = await fetch(
          `${CONFIG.BACKEND_URL}/short-url`,
          requestOptions
        )
          .then((data) => data.json())
          .catch((err) => console.error(err))
        console.log({ response })
      }
    }
    if (generateClick) {
      callApi()
    }
    return () => {
      setGenerateClick(false)
      setName("")
      setUrl("")
    }

    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [generateClick, props.loading])

  return (
    <div className="block p-6 rounded-lg shadow-lg bg-white max-w-sm">
      <h2 className="font-mono">Generate short links</h2>
      <br />
      <div className="flex m-auto form-group mb-6">
        <input
          type="url"
          className="form-control block
          w-full
          px-3
          py-1.5
          text-base
          font-normal
          text-gray-700
          bg-white bg-clip-padding
          border border-solid border-gray-300
          rounded
          transition
          ease-in-out
          m-0
          focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
          id="nameInput"
          placeholder="Name (optional)"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
      </div>
      <div className="flex m-auto form-group mb-6">
        <input
          type="url"
          className="form-control block
          w-full
          px-3
          py-1.5
          text-base
          font-normal
          text-gray-700
          bg-white bg-clip-padding
          border border-solid border-gray-300
          rounded
          transition
          ease-in-out
          m-0
          focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none"
          id="urlInput"
          placeholder="URL Link"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
        />
      </div>
      <button
        onClick={handleClick}
        className="
        w-full
        px-6
        py-2.5
        bg-blue-600
        text-white
        font-medium
        text-xs
        leading-tight
        uppercase
        rounded
        shadow-md
        hover:bg-blue-700 hover:shadow-lg
        focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0
        active:bg-blue-800 active:shadow-lg
        transition
        duration-150
        ease-in-out"
      >
        Generate
      </button>
    </div>
  )
}

export default InputBox
