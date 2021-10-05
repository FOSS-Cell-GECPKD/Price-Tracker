import React from 'react'

export const Credentials = () => {
    return (
        <div>
            <form className="form">
                <input
                    type='text'
                    name='text'
                    placeholder='Enter your name'
                    autoComplete="off"


                />
                <input
                    type='text'
                    name='text'
                    placeholder='Email-id'
                    autoComplete="off"


                />
                <input
                    type='text'
                    name='text'
                    placeholder='Product name'
                    autoComplete="off"

                />
                <input
                    type='text'
                    name='text'
                    placeholder='Down price'
                    autoComplete="off"

                />
                <input
                    type='submit'
                    value='Submit'
                    className='btn btn-dark btn-block'
                />

            </form>
        </div>
    )
}

export default Credentials