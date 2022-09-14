import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode } from "react"
import Select from '@material-ui/core/Select';
import {styled} from "@material-ui/core/styles";

interface State {
  selectedOptions: string[]
}

class StMuiMultiselect extends StreamlitComponentBase<State> {
  public state = { selectedOptions: [] }

  /** Method for rendering the component */
  public render = (): ReactNode => {
    const options: string[] = this.props.args["options"]

    const vMargin = 10
    const hMargin = 10
    const StyledSelect = styled(Select)({
      margin: `${vMargin}px ${hMargin}px`,
      width: this.props.width - hMargin * 2
    });

    return (
      <span>
        <StyledSelect
          labelId="demo-mutiple-checkbox-label"
          id="demo-mutiple-checkbox"
          multiple
          native
          value={this.state.selectedOptions}
          onChange={this.onChange}
          inputProps={{
            id: 'select-multiple-native',
          }}
          //SelectDisplayProps={{ style: { paddingTop: 10, paddingBottom: 8 } }}
          disabled={this.props.disabled}
        >
          {options.map((option) => (
            <option key={option} value={option}>
              {option}
            </option>
          ))}
        </StyledSelect>
      </span>
    )
  }

  /** Called when user selects items. Update JS State as well as streamlit component state  */
  private onChange = (event: any): void => {
    const { options } = event.target as HTMLSelectElement;
    const value: string[] = [];
    for (let i = 0, l = options.length; i < l; i += 1) {
      if (options[i].selected) {
        value.push(options[i].value);
      }
    }
    this.setState(
        prevState => ({ selectedOptions: value }),
        () => Streamlit.setComponentValue(this.state.selectedOptions)
    )
  }
}

export default withStreamlitConnection(StMuiMultiselect)
