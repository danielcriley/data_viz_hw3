class ChartForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      zipcode: ''
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({
      [event.target.name]: event.target.value
    });
  }

  handleSubmit(event) {
    // var spec = "https://gist.githubusercontent.com/hvo/8febd426e3d12bd430aedc0cd8dd1d41/raw/766342b5a84455fb941607eede525a3b7193946a/DV_Lab7.vg.json";
    var spec = `/chart/${this.state.zipcode}`;
    vegaEmbed('#vis', spec, {actions:false});
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          Zipcode: 
          <input 
            type='text'
            name='zipcode'
            list='all_zipcodes'
            value={this.state.zipcode} 
            onChange={this.handleChange} /> 

          <datalist id="all_zipcodes">
              {all_zipcodes.map((item) =>
                  <option value={item} />
              )}
          </datalist>

        </label> 
        <input type="submit" value="Update" />
      </form>
    );
  }
}

ReactDOM.render(
  <div>
    <ChartForm />
  </div>,
  document.getElementById('ui')
);