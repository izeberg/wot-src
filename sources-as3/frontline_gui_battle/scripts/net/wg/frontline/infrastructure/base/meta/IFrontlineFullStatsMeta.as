package net.wg.frontline.infrastructure.base.meta
{
   import flash.events.IEventDispatcher;
   
   public interface IFrontlineFullStatsMeta extends IEventDispatcher
   {
       
      
      function as_initializeText(param1:String, param2:String) : void;
      
      function as_setIsInteractive(param1:Boolean) : void;
      
      function as_setGeneralBonus(param1:Number) : void;
   }
}
