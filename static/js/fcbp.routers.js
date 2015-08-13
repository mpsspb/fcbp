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
    }).when('/periods', {
      controller: 'PeriodsController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/products/periods.html'
    }).when('/clubcards', {
      controller: 'ClubCardsController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/products/clubcards.html'
    }).when('/aqua-aerobics', {
      controller: 'AquaAerobicsController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/products/aqua-aerobicses.html'
    }).when('/sports', {
      controller: 'SportsController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/products/sports.html'
    }).when('/clients', {
      controller: 'ClientsController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/clients/clients.html'
    }).when('/new-clients', {
      controller: 'NewClientController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/clients/new-client.html'
    }).when('/cardclient/:uid', {
      controller: 'ClientCardController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/clients/card-client.html'
    }).when('/', {
      controller: 'StartController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/index.html'
    }).otherwise('/');
  }
})();