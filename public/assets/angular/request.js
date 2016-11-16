var app = angular.module("mainModule", []);

app.controller("controller",function($scope,$http){

	$scope.search = function(){
		$http.post("search?"+$scope.acidez+"?"+$scope.ph+"?"+$scope.alcohol)
		.success(function(data){
			alert(data);
			$scope.respuesta = data;
		})
		.error(function(err){
			alert('Error en el servidor. Contacte con el administrador.');
		})
	}
});