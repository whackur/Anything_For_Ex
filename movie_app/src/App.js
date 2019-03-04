import React, { Component } from 'react';
import './App.css';
import Movie from './Movie';

const movies = [
  {
    title : "Matrix",
    poster : "http://ojsfile.ohmynews.com/STD_IMG_FILE/2016/1130/IE002061432_STD.jpg"
  },
  {
    title : "Full Metal Jacket",
    poster : "http://image.cine21.com/resize/cine21/poster/2009/1007/M0010010_[X230,330].jpg"
  },
  {
    title : "Old boy",
    poster : "http://artinsight.co.kr/n_news/peg/1508/thumb/a4cb4757610239a28cf0cba125b24a69_vpZESkDO68sOb6AbZkW9hFd.jpg"
  },
  {
    title : "Star Wars",
    poster : "http://moonhak.co.kr/home/wp-content/uploads/bookcover/%EC%8A%A4%ED%83%80%EC%9B%8C%EC%A6%88-%EC%94%A8%EB%84%A4%EC%95%84%ED%8A%B84_%ED%91%9C1_web.jpg"
  }
]

class App extends Component {
  state = {
    greeting : "Hello!"
  }

  componentDidMount(){
    setTimeout(() => {
      this.setState({
        greeting : "Hello Again!"
      })
    },2000)
  }

  render() {
    return (
      <div className="App">
        {this.state.greeting}
        {movies.map((movie, index) => {
          return <Movie title={movie.title} poster={movie.poster} key={index} />
        })}
      </div>
    );
  }
}

export default App;
