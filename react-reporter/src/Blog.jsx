import React from 'react';
import Article from './Article';

class Blog extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            isPublished: false
        }
    }

    // 公開状態を変更
    togglePublished = () => {
        this.setState( {
            isPublished: !this.state.isPublished
        })
    };

    render(){
        return (
            <>
                <Article title={"reporter"} isPublished={this.state.isPublished} toggle={() => this.togglePublished()} />
            </>
        )
    }
}

export default Blog;