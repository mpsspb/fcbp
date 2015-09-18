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
    }).when('/clients', {
      controller: 'ClientsController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/clients/clients.html'
    }).when('/new-client', {
      controller: 'NewClientController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/clients/new-client.html'
    }).when('/new-client-product/:uid', {
      controller: 'NewClientProductController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/clients/new-client-product.html'
    }).when('/cardclient/:uid', {
      controller: 'ClientCardController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/clients/card-client.html'
    }).when('/employees', {
      controller: 'EmployeesController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/employees/employees.html'
    }).when('/positions', {
      controller: 'PositionsController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/employees/positions.html'
    }).when('/usecardclient/:uid', {
      controller: 'UseClientCardController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/clients/use/clubcard.html'
    }).when('/useaquaaerobics/:uid', {
      controller: 'UseClientAquaController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/clients/use/aquaaerobics.html'
    }).when('/useticket/:uid', {
      controller: 'UseClientTicketController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/clients/use/ticket.html'
    }).when('/usepersonal/:uid', {
      controller: 'UseClientPersonalController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/clients/use/personal.html'
    }).when('/usetiming/:uid', {
      controller: 'UseTimingController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/clients/use/timing.html'
    }).when('/', {
      controller: 'StartController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/index.html'
    })
    .otherwise('/');
  }
})();