package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _9ccc27928f4591e32c817a59d6773cb27f093547639ff600257daae44f87c49a_flash_display_Sprite extends Sprite
   {
       
      
      public function _9ccc27928f4591e32c817a59d6773cb27f093547639ff600257daae44f87c49a_flash_display_Sprite()
      {
         super();
      }
      
      public function allowDomainInRSL(... rest) : void
      {
         Security.allowDomain.apply(null,rest);
      }
      
      public function allowInsecureDomainInRSL(... rest) : void
      {
         Security.allowInsecureDomain.apply(null,rest);
      }
   }
}
