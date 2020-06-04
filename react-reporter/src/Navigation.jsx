import React from 'react';
import {AppBar, Drawer, MenuItem, Toolbar} from 'material-ui';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';

export class Navi extends React.Component {
    constructor () {
        super();
        this.state = {
            open: false
        }
        this.handleToggle = this.handleToggle.bind(this)
    }
       
    handleToggle() {
        console.log('Handle Toggle')
        this.setState({open: !this.state.open}) 
    }

    render () {
        return (
        <MuiThemeProvider>
            <div>
                <Drawer
                    open={this.state.open}
                    docked={false}
                    width={200}
                    onRequestChange={this.handleToggle}
                >
                <MenuItem>ログアウト</MenuItem>
                </Drawer>
                <AppBar title="Sample React"
                      onLeftIconButtonClick={this.handleToggle}>
              </AppBar>
            </div>
        </MuiThemeProvider>
        )
    }
}