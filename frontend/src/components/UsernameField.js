import React from 'react';
import {FormControl, form, FormGroup} from 'react-bootstrap';

const UsernameField = (props) => {


  return(
    <div className="container">
      <form>
        <FormGroup controlId="formBasicText">
          <FormControl type="text" className="form-control" placeholder="Your Spotify username" name="search" />
          <br />
          <FormControl type="text" className="form-control" placeholder="Your friend's Spotify username" name="search" />
            <br />
            <div className="container">
              <button type="button" className="btn btn-primary" >Search</button>
            </div>
        </FormGroup>
      </form>
    </div>
  )
}

export default UsernameField;
