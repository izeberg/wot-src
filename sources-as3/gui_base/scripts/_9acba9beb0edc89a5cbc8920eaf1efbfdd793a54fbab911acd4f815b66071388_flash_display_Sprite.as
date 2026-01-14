package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _9acba9beb0edc89a5cbc8920eaf1efbfdd793a54fbab911acd4f815b66071388_flash_display_Sprite extends Sprite
   {
       
      
      public function _9acba9beb0edc89a5cbc8920eaf1efbfdd793a54fbab911acd4f815b66071388_flash_display_Sprite()
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
