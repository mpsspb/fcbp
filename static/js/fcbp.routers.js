(function () {
  'use strict';

  angular
    .module('fcbp.routes', ['ngRoute']);
    
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
    }).when('/products', {
      controller: 'ProductsController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/products/products.html'
    }).when('/clients', {
      controller: 'ProductsController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/clients/clients.html'
    }).when('/', {
      controller: 'StartController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/index.html'
    }).otherwise('/');
  }
})();