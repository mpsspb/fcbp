(function () {
  'use strict';

  angular
    .module('fcbp.product.routes', ['ngRoute']);
    
  angular
    .module('fcbp.product.routes')
    .config(config);

  config.$inject = ['$routeProvider'];

  /**
  * @name config
  * @desc Define valid application routes
  */
  function config($routeProvider) {
    $routeProvider.when('/products', {
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
    }).when('/training', {
      controller: 'TrainingController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/products/training.html'
    }).when('/discounts', {
      controller: 'DiscountsController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/products/discounts.html'
    }).when('/cardtexts', {
      controller: 'CardTextController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/products/cardtexts.html'
    }).when('/tickets', {
      controller: 'TicketsController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/products/tickets.html'
    }).when('/timing', {
      controller: 'TimingController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/products/timings.html'
    }).when('/personals', {
      controller: 'PersonalsController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/products/personals.html'
    });
  }
})();