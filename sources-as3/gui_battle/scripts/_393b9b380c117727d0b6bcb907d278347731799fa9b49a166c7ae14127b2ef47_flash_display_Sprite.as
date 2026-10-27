package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _393b9b380c117727d0b6bcb907d278347731799fa9b49a166c7ae14127b2ef47_flash_display_Sprite extends Sprite
   {
       
      
      public function _393b9b380c117727d0b6bcb907d278347731799fa9b49a166c7ae14127b2ef47_flash_display_Sprite()
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
