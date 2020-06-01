# Angular

Angular is used as a front end tool to create a webbased application
Angular mainly works as a Component based modules

### Component 
Generally the component consist of root component which is appcomponent and sub component which we will be creating by ourself
to create a component       -  ng create component [component name] or ng c g [component name] (eg : ng c g mypage)
this will create a folder with the component name which we have and it consist of 5 files in general
1. mypage.component.html : html content goes here
2. mypage.component.scss :  the styles comes here
3. mypage.component.ts : selector, templateurl and style url we have declare here and also the business logic comes here. selector - the tag, tempplateurl - the folde,anr path of the file without extension
4. mypage.module.ts : have to give the other component info to integrate the other component respectively
5. mypage.component.spec.ts : (unknown as of now)

### Databinding
databinding is nothing but connecting the template and type script(business logic)
it of three types
* connect from ts to template - 1. String Interpolation   ---->  {{ data }}
                                2. property binding     ------>  [property]="data"
 
* Connect from template to ts(event capture) - event binding  ----> (event) = "expression"
* Two way binding  - [(ngModel}] = "data"

                             

