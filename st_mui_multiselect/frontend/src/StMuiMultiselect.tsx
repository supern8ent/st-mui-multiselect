import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode } from "react"
import Select from '@material-ui/core/Select';
import Input from '@material-ui/core/Input';
import MenuItem from '@material-ui/core/MenuItem';
import Checkbox from '@material-ui/core/Checkbox';
import ListItemText from '@material-ui/core/ListItemText';
import {styled} from "@material-ui/core/styles";

interface State {
  selectedOptions: string[]
}


class StMuiMultiselect extends StreamlitComponentBase<State> {
  public state = { selectedOptions: [] }

  public render = (): ReactNode => {
    const vMargin = 200
    const hMargin = 25
    const StyledSelect = styled(Select)({
      margin: `${vMargin}px ${hMargin}px`,
      width: this.props.width - hMargin * 2
    });

    const options: string[] = this.props.args["options"]
    const checkered: string[] = this.state.selectedOptions

    return (
      <span>
        <StyledSelect
          labelId="demo-mutiple-checkbox-label"
          id="demo-mutiple-checkbox"
          multiple
          value={this.state.selectedOptions}
          onChange={this.onChange}
          input={<Input />}
          renderValue={(selected: any) => (selected as string[]).join(', ')}
          //MenuProps={MenuProps}
        >
          {options.map((option: string) => (
            <MenuItem key={option} value={option}>
              <Checkbox checked={checkered.includes(option)} />
              <ListItemText primary={option} />
            </MenuItem>
          ))}
        </StyledSelect>
      </span>
    )
  }

  private onChange = (event: any): void => {
    console.log(event.target.value)
    this.setState(
        prevState => ({ selectedOptions: event.target.value }),
        () => Streamlit.setComponentValue(this.state.selectedOptions)
    )
  }
}

export default withStreamlitConnection(StMuiMultiselect)
