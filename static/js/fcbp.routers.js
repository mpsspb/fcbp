(function () {
  'use strict';

  angular
    .module('fcbp.routes')
    .config(config);

  config.$inject = ['$routeProvider'];

  /**
  * @name config
  * @desc Define valid application routes
  */
  function config($routeProvider) {
    $routeProvider.when('/login', {
      controller: 'LoginController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/login.html'
    }).when('/', {
      controller: 'IndexController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/index.html'
    }).when('/products', {
      controller: 'ProductsController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/products/index.html'
    }).otherwise('/');
  }
})();