(function () {
  'use strict';

  angular
    .module('fcbp.employees', [
      'fcbp.employees.controllers',
      'fcbp.employees.services',
      'fcbp.employee.directives',
      'fcbp.positions.controllers',
    ]);

  angular
    .module('fcbp.employees.controllers', []);

  angular
    .module('fcbp.employees.services', []);

  angular
    .module('fcbp.employee.directives', []);

  angular
    .module('fcbp.positions.controllers', []);


})();